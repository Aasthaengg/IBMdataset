#整数の入力
N = int(input())

#スペース区切りの整数の入力リスト
A_list = list(map(int, input().split()))

A_list = list(reversed(sorted(A_list)))
#print(A_list)



ans  = 0
for i in range(1,2*N,2):
  ans = ans + A_list[i]
print(ans)