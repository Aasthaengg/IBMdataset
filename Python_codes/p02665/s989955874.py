N = int(input())
nums = list(map(int, input().split()))
nodes = []
currentLeaf = 1
fail = False
#check from top
for i in range(N + 1):
	nodes.append(currentLeaf)
	currentLeaf = (currentLeaf-nums[i])*2
	if (currentLeaf < 0):
		fail = True
		break 
if (fail):
	print(-1)
else:
  #check from bottom
  currentLeaf = 0
  totalNode = 0
  for i in reversed(range(N+1)):
      currentLeaf += nums[i]
      currentLeaf = min(currentLeaf, nodes[i])
      totalNode += currentLeaf

  if (fail):
      print(-1) 
  else:
      print(totalNode)