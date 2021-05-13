def main():
 n = list(map(int,input().split()))
 n.sort()
 n.reverse()
 print(n[0] * 10 + n[1] + n[2])

main()