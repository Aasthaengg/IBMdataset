H, W = map(int, input().split())
h, w = map(int, input().split())

start_state = H * W
deduct_state = h * W + w * H - h * w

answer = start_state - deduct_state

print(answer)
