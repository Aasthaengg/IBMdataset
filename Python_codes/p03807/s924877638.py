N = int(input())
al = [int(a) for a in input().split()]

odd_num = sum([1 for a in al if a % 2 == 1])
even_num = len(al) - odd_num

ans = "YES"
if odd_num % 2 == 1:
    ans = "NO"
if odd_num == 1 and even_num == 0:
    ans = "YES"

print(ans)