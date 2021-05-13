abc = list(map(int, input("").split()))
k = int(input())

abc.sort(reverse=True)

abc[0] = abc[0] * (2 ** k)

print(sum(abc))