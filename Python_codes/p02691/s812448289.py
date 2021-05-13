N = int(input())
A = [int(i) for i in input().split()]

# 線形で計算できる
# j > iとしてA[j]+A[i] = j-iよりA[i]+i=j-A[j]
# iとjを分離できたのでjを前に進めていって、計算結果を貯めていけばいい
# 

counter = 0
dic = {}
for j in range(N):
    if j-A[j] in dic:
        counter += dic[j - A[j]]
    if j + A[j] in dic:
        dic[j+A[j]] += 1
    else:
        dic[j+A[j]] = 1
print(counter)
