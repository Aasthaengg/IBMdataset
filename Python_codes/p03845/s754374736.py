prob = int(input())
sec = [int(n)for n in input().split()]
su = sum(sec)
for _ in range(int(input())):
    p, x = map(int, input().split())
    print(su - sec[p - 1] + x)
