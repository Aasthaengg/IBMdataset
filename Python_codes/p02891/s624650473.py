s = input()
K = int(input())

if s == (s[0]*len(s)):
    print((len(s)*K)//2)

elif s[0] == s[-1]:
    front = 0
    back = len(s)-1
    for i in range(len(s)-1):
        if s[i] is s[i+1]:
            front += 1
        else:
            break

    for i in range(len(s)-1, 1, -1):
        if s[i] == s[i-1]:
            back -= 1
        else:
            break
    
    s_front = s[:front+1]
    s_back = s[back:]
    s_middle = s[front+1:back]

    new_s = s_middle + s_back + s_front
            
    ans = 0
    cnt = 1
    for i in range(len(new_s)-1):
        if new_s[i] == new_s[i+1]:
            cnt += 1
        else:
            ans += cnt//2
            cnt = 1
    ans += cnt//2
    ans *= K-1

    cnt = 1
    for i in range(len(s_middle)-1):
        if s_middle[i] == s_middle[i+1]:
            cnt += 1
        else:
            ans += cnt//2
            cnt = 1
    ans += cnt//2
    ans += (front+1)//2 + (len(s)-back)//2
    print(ans)
    
else:
    ans = 0
    cnt = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += cnt//2
            cnt = 1
    ans += cnt//2
    ans *= K
    print(ans)