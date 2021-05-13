# C - Scc Puzzle
def main():
    n, m = map(int, input().split())


    if m-n*2 >= 0:
        print(n+((m-n*2)//4))
    else:
        print(m//2)
  
        
if __name__ == '__main__':
    main()