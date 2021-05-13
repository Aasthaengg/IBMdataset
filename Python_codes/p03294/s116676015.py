import fractions
def lcm(a, N):
  ans = a[0]
  for i in range(1, N):
      ans = ans * a[i] // fractions.gcd(ans, a[i])
  return ans
 
def main():
  N = int(input())
  A = list(map(int,input().split()))
  num = lcm(A, N) - 1
  answer = 0
  for i in A:
    answer += num % i
  print(answer)

if __name__=='__main__':
    main()