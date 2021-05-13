def main():
  N = int(input())
  cuisine =  []
  for i in range(N):
    a,b = map(int, input().split())
    cuisine.append([a+b, a, b])
  cuisine.sort(key = lambda x:x[0], reverse = True)
  happy_t = 0
  happy_a = 0
  for i in range(N):
    if i % 2 == 0:
      happy_t += cuisine[i][1]
    else:
      happy_a += cuisine[i][2]
  print(happy_t-happy_a)
  
if __name__ == "__main__":
  main()