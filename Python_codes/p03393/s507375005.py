s=str(input())
a=list("zyxwvutsrqponmlkjihgfedcba")
a=a[::-1]
#print(a)


if "zyxwvutsrqponmlkjihgfedcba"==s:
    print(-1)
    exit()


if len(s)==26:
    s=s[::-1]#後ろから見ていく
    for i in range(len(s)):
        for j in range(i+1):
            #print(i,j,s[i],s[j])
            if s[i]<s[j]:#xyzの降順の流れが切れたところを変える
                s=s[::-1]
               # print(s)
                print(s[:-(i+1)]+s[-(j+1)])
                exit()
else:
    for i in a:
        if i not in s:
            s+=i
            break
    print(s)

