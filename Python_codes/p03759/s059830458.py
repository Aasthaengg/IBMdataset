def INSTR():
	return input()

def INNUM():
	return int(INSTR())

def INSTR_S():
	return INSTR().split()

def INNUM_S():
	return map(int, INSTR_S())

def INSTR_SM(n):
	return [tuple(INSTR_S()) for _ in range(n)]

def INNUM_SM(n):
	return [tuple(INNUM_S()) for _ in range(n)]

A, B, C = INNUM_S()
print("YNEOS"[(B-A)!=(C-B)::2])