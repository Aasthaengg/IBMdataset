dic = {}
S, T = input().split()
A, B = map(int, input().split())
dic[S] = A
dic[T] = B
U = input()
dic[U] -= 1
print(dic[S], dic[T])