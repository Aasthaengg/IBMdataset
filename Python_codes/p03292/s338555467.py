def main():
 a = list(map(int,input().split()))
 ans = 0
 a.sort()
 for i in range(2):
     ans += abs(a[i] - a[i + 1])
 print(ans)
main()