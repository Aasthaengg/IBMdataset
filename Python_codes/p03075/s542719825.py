def main():
    a = [int(input()) for _ in range(5)]
    k = int(input())
    print("Yay!" if a[-1]-a[0] <= k else ":(")
    
if __name__ == "__main__":
    main()