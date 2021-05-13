N,K = list(map(int,input().split()))
S = input()
S_list = list(S)
K -= 1
answer = ""
S_list[K] = S_list[K].swapcase()

for x in S_list:
    answer += x
print(answer)