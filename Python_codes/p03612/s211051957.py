n=int(input())
p= list(map(int,input().split()))
cnt=0
cnt2 = 0
c = 1.1
for i in range(n):
    if p[i] == i+1:
        cnt += 1
        if i - c == 1:
            cnt2 += 1
            c = 1.1
        else:
            c = i
ans = (cnt-2*cnt2) + cnt2
print(ans)
