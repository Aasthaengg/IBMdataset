H, W, N = int(input()),int(input()),int(input())
HW=[H,W][H<W]
NdivHW=N/HW
NdivHW=int(NdivHW)+([0, 1][NdivHW%1>0])
print(NdivHW)