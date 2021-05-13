def main():
    x, y = map(int, input().split())
    
    count = 1
    while True:
        x *= 2
        
        if x > y:
            break
        else:
            count += 1
            
    print(count)
    

if __name__ == '__main__':
    main()