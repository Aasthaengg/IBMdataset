def main():
 a,b = map(int,input().split())
 if a <= 12 and a >= 6:
     print(b // 2)
 elif a < 6:
     print(0)
 else:
     print(b)
main()