import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    H, A = MI()


    if H<=A:
        print(1)
    elif H%A==0:
        print(H//A)
    else:
        print((H//A)+1)


if __name__ == "__main__":
	main()