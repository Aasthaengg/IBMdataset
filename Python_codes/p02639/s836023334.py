from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())

def main():
    print(i_list().index(0) + 1)

if __name__ == "__main__":
    main()
