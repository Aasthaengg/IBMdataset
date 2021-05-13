A=int(input())
n_l= list(map(int,input().split()))
n_a = [i for i in n_l if i % 2 == 0 and i % 4 != 0]
n_b = [i for i in n_l if i % 4 == 0]
ans = len(n_b)*2+1
if len(n_a) > 0:
    ans+=len(n_a)-1
if A <= ans:
    print("Yes")
else:
    print("No")