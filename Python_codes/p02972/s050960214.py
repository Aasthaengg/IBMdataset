N = int(input())
a = list(map(int,input().split()))
m_list = []
m_num = 0

ans_ls = [0]*N
for i in range(N):
    temp = 0
    num = N - i
    j = 1
    while num*j <= N:
        temp += ans_ls[num*j-1]
        j += 1
    if (temp + a[num-1])%2 == 1:
        ans_ls[num-1] = 1
        m_list.append(str(num))
        m_num += 1
m_list.sort()

print(m_num)
print(' '.join(m_list))

