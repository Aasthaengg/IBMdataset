n = int(input())
print(min(bin(int(i))[::-1].find("1") for i in input().split()))