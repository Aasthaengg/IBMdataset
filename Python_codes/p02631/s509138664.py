def main():
   n = int(input())
   a = list(map(int,input().split()))
   b = [0 for i in range(n)]
   c = 0
   for i in range(n):
       c ^= a[i]
   for i in range(n):
       b[i] = c ^ a[i]
   for i in range(n):
       if i == n - 1:
           print(b[i])
       else:
           print(b[i], end = ' ')
main()