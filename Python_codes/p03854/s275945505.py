s = input()
pat_list = ["dream","dreamer","erase","eraser"]

while 1:
    flag=0
    for p in pat_list:
        if s.endswith(p):
            flag=1
            s = s[:-len(p)]
    if not s:
        print("YES")
        break
    if not flag:
        print("NO")
        break
