N = int(input())
A = list(map(int,input().split()))

# N = 10**5
# A = [random.randint(0,1) for _ in range(N)]
# print('A:',A)

ans_ = [0]*(N+1)

for n1 in range(N,0,-1):
    a = A[n1-1]
    sum_ = 0
    for n2 in range(2*n1,N+1,n1):
        sum_ += ans_[n2]
    if sum_%2 == a:
        ans_[n1] = 0
        
    elif sum_%2 != a:
        ans_[n1] = 1
        
# print('ans_:',ans_)

ans_list = []  
for s_ in range(len(ans_)):
    s=ans_[s_]
    if s == 1:
        ans_list.append(s_)
        
print(len(ans_list))
if len(ans_list)>0:
    print(' '.join(map(str,ans_list)))