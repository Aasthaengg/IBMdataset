
def main():
    
    kinds = list(map(int,input().split()))
    prices = list(map(int,input().split()))
    
    minPrice = 0
    
    for item in range(kinds[1]):
        minPrice += min(prices)
        prices.remove(min(prices))

    print(minPrice)         
    
  

if __name__ == "__main__":
    main()