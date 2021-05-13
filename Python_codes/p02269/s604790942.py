#!/usr/bin/env python
#-*- coding:utf-8 -*-

ARRY_SIZE = 1000003

def hash1(key):
	return key % (ARRY_SIZE)

def hash2(key):
	return 1 + (key % (ARRY_SIZE - 1))

def hash_combo(key, i):
	return (hash1(key) + i * hash2(key)) % ARRY_SIZE

def insert(arr,key):
	i = 0

	while True:
		j = hash_combo(key, i)
		if arr[j] == "":
			arr[j] = key
			return True
		else:
			i +=  1

def find(arr, key):
	i = 0
	while True:
		j = hash_combo(key,i)
		if arr[j] == key:
			return True
		elif arr[j] == "" or i >= ARRY_SIZE:
			return False
		else:
			i += 1

def getKey(pre_key):
	key =[]
	for pk in pre_key:
		if pk == "A":
			key.append(1)
		elif pk == "C":
			key.append(2)
		elif pk == "G":
			key.append(3)
		else:
			key.append(4)
	return int("".join(map(str,key)))
		
	


def main():
	N = int(raw_input())
	cmd = [raw_input().split() for _ in range(N)]
	dic = [""] * ARRY_SIZE

	for i in range(N):
		if cmd[i][0] == "insert":
			insert(dic, getKey(cmd[i][1]))
		elif cmd[i][0] == "find":
			if find(dic, getKey(cmd[i][1])):
				print "yes"
			else:
				print "no"



#def test():

if __name__ == '__main__':
	main()
	#test()