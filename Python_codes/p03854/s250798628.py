S = input().strip()
N = len(S)
cur = 0
flag = 0
while cur<N:
    if S[cur:cur+5]=="dream":
        if cur+5==N:
            cur += 5
        elif cur+5<N and S[cur+5]=="d":
            cur += 5
        elif S[cur:cur+7]=="dreamer":
            if cur+7==N:
                cur += 7
            elif S[cur+7] in ["d","e"]:
                cur += 7
            elif S[cur+7]=="a":
                cur += 5
            else:
                flag = 1
                break
        else:
            flag=1
            break
    elif S[cur:cur+5]=="erase":
        if cur+5==N:
            cur += 5
        elif cur+5<N and S[cur+5]=="r":
            cur += 6
        elif cur+5<N and S[cur+5] in ["d","e"]:
            cur += 5
        else:
            flag = 1
            break
    else:
        flag=1
        break
if flag==0:
    print("YES")
else:
    print("NO")