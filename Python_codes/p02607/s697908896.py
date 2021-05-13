
def main():
    
    n = int(input())
    
    Numbers = list(map(int,input().split()))
    count = 0
    for item in range(1,n+1):
        if item % 2 != 0 and Numbers[item-1] % 2 != 0:
            count += 1
    
    print(count)
        
    
  

if __name__ == "__main__":
    main()