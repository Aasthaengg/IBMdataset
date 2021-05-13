N = int(input())
[T, A] = list(map(int, input().split()))
list_H0 = list(map(int, input().split()))
list_H1 = []
for i in list_H0:
  list_H1.append(T - i*0.006)
list_HA = []
for k in list_H1:
  list_HA.append(abs(A - k))
Min = min(list_HA)
print(list_HA.index(Min) + 1)