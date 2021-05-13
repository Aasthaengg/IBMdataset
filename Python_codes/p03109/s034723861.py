def main():
    s = list(map(int, input().split("/")))
    if s[0] > 2019:
        print("TBD")
        return
    
    if s[1] > 4:
        print("TBD")
        return

    # 必要??
    if s[2] > 30:
        print("TBD")
        return

    print("Heisei")

if __name__ == "__main__":
    main()
