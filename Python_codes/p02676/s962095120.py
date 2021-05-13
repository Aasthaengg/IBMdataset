K=int(input())
S=str(input())

def answer(a:int,b:str):
    if len(b)<=a:
        return(b)
    else:
        return (b[0:a]+"...")

print(answer(K,S))