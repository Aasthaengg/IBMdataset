def main():
 a,b,x = map(int,input().split())
 if a == x or (a < x and a + b >= x):
     print('YES')
 else:
     print('NO')
main()