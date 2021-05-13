import heapq
def mium():
  hen = list(map(int, input().split()))
  hens = heapq.nsmallest(2, hen)
  print(int(hens[0]*hens[1]/2))
if __name__ == "__main__":
  mium()