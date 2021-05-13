
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    T=["AKIHABARA","KIHABARA","AKIHBARA","AKIHABRA","AKIHABAR","KIHBARA","KIHABRA","KIHABAR","AKIHBRA","AKIHABR","AKIHABAR","AKIHBR","KIHABR","KIHBAR","KIHBRA","KIHBR"]
    
    flag=0
    for i in range(len(T)):
        if S==T[i]:
            flag=1
        

    
    
    if flag==0:
        print("NO")
    else:
        print("YES")

main()
