s=input()
n=len(s)
#print(n)
ans=0
for bit in range(1 << (n - 1)):
    # 各場合で式 f を生成する
    #print("bit",bit,bin(bit))
    f = s[0]

    for i in range(n - 1):
        if bit & (1 << i):
            # フラグが立っているならば "+" を式の末尾に追加する
            f += "+"
        else:
          f+="-"
        f += s[i + 1]
        #print("i",i,"1 << i",bin(1 << i),"f",f)
    #print(f)
    ans=eval(f)
    if ans==7:
      f+="=7"
      print(f)
      exit()
