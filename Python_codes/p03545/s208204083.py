S= input()
List=list(S)
mid=int(List[0])
opList = ["+"]*3
res="a"
# 010 なら2番目のみ派閥 
for bits in range(2**3): 
  for j in range(3):
    if((bits>>j) & 1):
      opList[j] = "+"
      mid = mid + int(List[j+1])
    else:
      opList[j] = "-"
      mid = mid - int(List[j+1])
  if mid == 7:
    res = List[0]+opList[0]+List[1]+opList[1]+List[2]+opList[2]+List[3]+"=7"
    break
  else:
    mid = int(List[0])
    opList = ["+"]*3
print(res)