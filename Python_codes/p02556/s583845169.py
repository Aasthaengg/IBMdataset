def main():
  n = int(input())
  a_li , b_li = [] , []
  for _ in range(n):
    x , y = map(int,input().split())
    a_li.append(x + y)
    b_li.append(x - y)
  print(max(max(a_li) - min(a_li), max(b_li) - min(b_li)))
 
if __name__ == "__main__":
  main()