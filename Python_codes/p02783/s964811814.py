H, A = map(int, input().split())

a_ = (H / A)
print(int(a_) if a_.is_integer() else int(a_)+1)
