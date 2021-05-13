def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    cost = 0
    
    if n <= k:
        cost += n * x
    elif n > k:
        cost += k * x + (n - k) * y
    print(cost)
    
  
if __name__ == '__main__':
  main()