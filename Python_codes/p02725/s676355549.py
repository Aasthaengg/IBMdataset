K, N = map(int, input().split())
aaa = list(map(int, input().split()))
dif = list(aaa[i + 1] - aaa[i] for i in range(N - 1))
dif.append(K - aaa[-1] + aaa[0])
print(K - max(dif))