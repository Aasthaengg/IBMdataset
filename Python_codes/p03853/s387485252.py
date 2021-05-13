def main():
    h, _ = map(int, input().split())
    c = [input() for _ in range(h)]
    for cn in c:
        print(f'{cn}\n{cn}')


if __name__ == "__main__":
    main()
