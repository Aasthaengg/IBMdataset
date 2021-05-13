def main():
    s,w = map(int,input().split())
    answer = "unsafe" if w >= s else "safe"
    print(answer)
if __name__ == '__main__':
    main()
