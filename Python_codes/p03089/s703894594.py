n = int(input())
B = [0]+list(map(int,input().split()))

ans_li = []
for i in range(n):
    for j in range(len(B)-1,0,-1):
        if j==B[j]:
            ans_li.append(B.pop(j))
            break
    else:
        print(-1);exit()
print('\n'.join(map(str,ans_li[::-1])))