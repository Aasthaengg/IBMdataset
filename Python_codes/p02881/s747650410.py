N = int(input())
lst = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        lst.append(int(N/i) + i)
print(min(lst)-2)