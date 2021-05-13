N = int(input())
H = list(map(int, input().split()))
H.reverse()
def main():
  for i in range(N-1):
    if (H[i+1] - H[i] >= 2):
      print("No")
      return
    if (H[i+1] - H[i] == 1):
      H[i+1] -= 1
  print("Yes")

main()