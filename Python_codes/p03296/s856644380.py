# AGC 026: A – Colorful Slimes 2
n = int(input())
a = [i for i in input().split()]

counter = 0

for i in range(1, n):
    if a[i] == a[i - 1]:
        a[i] = 'a'
        counter += 1

print(counter)