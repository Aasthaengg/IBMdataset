def main():
    k=int(input())
    k1 = len([i for i in range(k) if i % 2 == 0])
    print(k1*(k-k1))
    
if __name__ == "__main__":
    main()