import numpy as np
# def main():
#     N=input()
#     N=int(N)
#     A=input().split(" ")
#     A=np.array([int(i) for i in A]).astype(np.uint64)
#     # A=np.random.randint(0,100000,200000)
#     l=[]
#     A=np.sort(A)
#     A=np.flip(A).astype(np.uint64)
#     sum=0
#     for i,num in enumerate(A):
#         if i%2==0:
#             l=l+[num]
#             if i!=0:
#                 sum+=min(l[-2],l[0])
#         else:
#             l=[num]+l
#             sum+=min(l[1],l[-1])
#     print(int(sum))

# def main2():
#     N=input()
#     N=int(N)
#     A=input().split(" ")
#     A=np.array([int(i) for i in A]).astype(np.uint64)
#     # A=np.random.randint(0,100000,200000)
#     A=np.sort(A)
#     A=np.flip(A).astype(np.uint64)
#     sum=0
#     for i,num in enumerate(A):
#         if i==0:
#             l=A[0]
#             r=A[0]
#             continue
#         sum+=min(l,r)
#         if l<r:
#             r=num
#         else:
#             l=num
#     print(int(sum))

def main3():
    N=input()
    N=int(N)
    A=input().split(" ")
    A=np.array([int(i) for i in A]).astype(np.uint64)
    l=[]
    A=np.sort(A)
    A=np.flip(A).astype(np.uint64)
    sum=0
    for i,num in enumerate(A):
        if i==0:
            l.append(num)
            continue
        l1=np.array(l,dtype=np.uint64)
        l2=np.roll(l1,1)
        l1=l1.reshape(-1,1)
        l2=l2.reshape(-1,1)
        l1=np.concatenate([l1,l2],1)
        l2=l1.min(1)
        arg=l2.argmax()
        l=l[:arg+1]+[num]+l[arg+1:]
        sum+=l2[arg]

    print(int(sum))


def correct():
    N=input()
    N=int(N)
    A=input().split(" ")
    A=np.array([int(i) for i in A]).astype(np.uint64)
    l=[]
    A=np.sort(A).astype(np.uint64)
    sum=0
    for i in range(N-1):
        sum+=A[N-(i+1)//2-1]
    print(int(sum))

if __name__ == "__main__":
    # main3()
    correct()